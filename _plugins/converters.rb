module Jekyll
  class HaikuConverter < Converter
    def matches(ext)
      ext =~ /^\.hk$/i
    end

    def output_ext(ext)
      ".html"
    end

    def convert(content)
      haiku = false
      output = ""
      content.lines.each do |line|
        line.chomp!
        if line.empty?
          if haiku
            output << '</div>'
            haiku ^= true
          end
        else
          if !haiku
            output << '<div class="haiku">'
            haiku ^= true
          end
          output << '<p class="haiku-verse">' << line << '</p>'
        end
      end
      if haiku
        output << '</div>'
      end
      output
    end
  end
end
