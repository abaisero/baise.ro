module Jekyll

  class MathJaxBlockTag < Liquid::Tag
    def render(context)
      '<script type="math/tex; mode=display">'
    end
  end

  class MathJaxInlineTag < Liquid::Tag
    def render(context)
      '<script type="math/tex">'
    end
  end

  class MathJaxEndTag < Liquid::Tag
    def render(context)
      '</script>'
    end
  end

end

Liquid::Template.register_tag('math', Jekyll::MathJaxBlockTag)
Liquid::Template.register_tag('m', Jekyll::MathJaxInlineTag)
Liquid::Template.register_tag('endmath', Jekyll::MathJaxEndTag)
Liquid::Template.register_tag('em', Jekyll::MathJaxEndTag)

module Jekyll

  class MountainStartTag < Liquid::Tag
    def initialize(tag_name, muhammad, tokens)
      super
      @muhammad = muhammad.strip
    end

    def render(context)
      '<div class="mountain" muhammad="%s">' % @muhammad
    end
  end

  class MountainEndTag < Liquid::Tag
    def render(context)
      '</div>'
    end
  end

  class MuhammadTag < Liquid::Tag
    def initialize(tag_name, muhammad, tokens)
      super
      @muhammad = muhammad.strip
    end

    def render(context)
      '<span class="muhammad" id="%s"></span>' % @muhammad
    end
  end

end

Liquid::Template.register_tag('mountain', Jekyll::MountainStartTag)
Liquid::Template.register_tag('endmountain', Jekyll::MountainEndTag)
Liquid::Template.register_tag('muhammad', Jekyll::MuhammadTag)

