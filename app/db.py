from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey, UniqueConstraint, CheckConstraint, TypeDecorator
from sqlalchemy.orm import relationship, validates

import bcrypt


class PasswordHash(object):
    def __init__(self, hash_):
        assert len(hash_) == 60, 'bcrypt hash should be 60 chars.'
        assert hash_.count('$'), 'bcrypt hash should have 3x "$".'
        self.hash = str(hash_)
        self.rounds = int(self.hash.split('$')[2])

    def __eq__(self, candidate):
        """Hashes the candidate string and compares it to the stored hash."""
        if isinstance(candidate, basestring):
            if isinstance(candidate, unicode):
                candidate = candidate.encode('utf8')
            return bcrypt.checkpw(candidate, self.hash)
        return False

    def __ne__(self, candidate):
        return not self.__eq__(candidate)

    def __repr__(self):
        """Simple object representation."""
        return '<{}>'.format(type(self).__name__)

    @classmethod
    def new(cls, password, rounds):
        """Creates a PasswordHash from the given password."""
        if isinstance(password, unicode):
            password = password.encode('utf8')
        return cls(bcrypt.hashpw(password, bcrypt.gensalt(rounds)))


class Password(TypeDecorator):
    """Allows storing and retrieving password hashes using PasswordHash."""
    impl = String
    # impl = Text

    def __init__(self, rounds=12, **kwds):
        self.rounds = rounds
        super(Password, self).__init__(**kwds)

    def process_bind_param(self, value, dialect):
        """Ensure the value is a PasswordHash and then return its hash."""
        return self._convert(value).hash

    def process_result_value(self, value, dialect):
        """Convert the hash to a PasswordHash, if it's non-NULL."""
        if value is not None:
            return PasswordHash(value)

    def validator(self, password):
        """Provides a validator/converter for @validates usage."""
        return self._convert(password)

    def _convert(self, value):
        """Returns a PasswordHash from the given string.

        PasswordHash instances or None values will return unchanged.
        Strings will be hashed and the resulting PasswordHash returned.
        Any other input will result in a TypeError.
        """
        if isinstance(value, PasswordHash):
            return value
        elif isinstance(value, basestring):
            return PasswordHash.new(value, self.rounds)
        elif value is not None:
            raise TypeError(
                'Cannot convert {} to a PasswordHash'.format(type(value)))


Base = declarative_base()

friendship = Table('friendships', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), index=True),
    Column('friend_id', Integer, ForeignKey('users.id')),
    UniqueConstraint('user_id', 'friend_id', name='unique_friendships'),
    # CheckConstraint raises IntegrityError
    CheckConstraint('user_id != friend_id', name='self-awareness'),  
)


from flask import url_for


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(Password)

    friends = relationship('User',
                           secondary=friendship,
                           primaryjoin=id==friendship.c.user_id,
                           secondaryjoin=id==friendship.c.friend_id,
                           )

    @validates('password')
    def _validate_password(self, key, password):
        return getattr(type(self), key).type.validator(password)

    def as_json(self, with_friends=False):
        json = dict(
            username = self.username,
            href = url_for('user', username=self.username),
        )

        if with_friends:
            json['friends'] = [friend.as_json() for friend in self.friends]

        return json

    def befriend(self, *friends):
        for friend in friends:
            if friend not in self.friends:
                self.friends.append(friend)

    def unfriend(self, *friends):
        for friend in friends:
            try:
                self.friends.remove(friend)
            except ValueError:
                pass

    def __repr__(self):
        return '<User {}>'.format(self.username)


from sqlalchemy import create_engine
engine = create_engine('sqlite:///app/rubus.db')
engine.connect()
Base.metadata.create_all(engine)

from sqlalchemy.orm import Session
session = Session(bind=engine)


if __name__ == '__main__':

    from sqlalchemy.orm.exc import NoResultFound

    def get_or_make_user(username, password):
        try:
            user = session.query(User).filter(User.username==username).one()
        except NoResultFound:
            user = User(username=username, password=password)
            session.add(user)
        return user

    bais = get_or_make_user('bais', 'bais')
    manuel = get_or_make_user('manuel', 'manuel')
    andre = get_or_make_user('andre', 'andre')
    anto = get_or_make_user('anto', 'anto')

    bais.befriend(manuel)
    bais.befriend(andre)

    manuel.befriend(bais)
    manuel.befriend(anto)

    andre.befriend(bais)
    andre.befriend(anto)

    anto.befriend(manuel)
    anto.befriend(andre)

    session.commit()
