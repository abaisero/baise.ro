module Jekyll
  module AuthorizeFilter
    def surname(author, selection, mod)
      output = author[selection]
      if !(author =~ mod).nil?
        output = '<strong>' + output + '</strong>'
      end
      output
    end

    def authorize(input, author)
      sel_regex = /\w+/
      mod_regex = /#{author}/
      values = input.split('and')
      authors = surname(values.first, sel_regex, mod_regex)
      values[1...-1].each do |v|
        authors += ', ' + surname(v, sel_regex, mod_regex)
      end
      authors += ' and ' + surname(values.last, sel_regex, mod_regex)
      authors
    end
  end
end

Liquid::Template.register_filter(Jekyll::AuthorizeFilter)
