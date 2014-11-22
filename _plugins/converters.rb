module Jekyll
  class EmojiConverter < Converter
    def matches(ext)
      ext =~ /^\.hk$/i
    end

    def output_ext(ext)
      ".html"
    end

    def convert(content)
      # content.gsub(/:(?<emoji>\w*):/, '<img class="emoji" title=":\k<emoji>:" src="https://a248.e.akamai.net/assets.github.com/images/icons/emoji/\k<emoji>.png" height="20" width="20" align="absmiddle">')
      # '<div class="haiku">' << content.gsub(/(?<line>.+)/, '<p class="haiku-line">\k<line></p>') <<  '</div>'
      #
      # output = '<div class="haiku">'
      # content.each_line do |line|
      #   output << '<p class="haiku-line">' << line << '</p>'
      # end
      # output << '</div>'
      # return output
      #
      # output = '<div class="haiku">'
      haiku = false
      output = ""
      # content.split('\n').each do |line|
      content.lines.each do |line|
        line.chomp!
      # content.scan(/.*/).each do |line|
        # output << line << ':' << line.empty? << ':'
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
          output << '<p class="haiku-line">' << line << '</p>'
        end
      end
      if haiku
        output << '</div>'
      end
      return output
    end
  end
end

