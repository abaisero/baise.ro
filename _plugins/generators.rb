module Jekyll

  class IpythonGenerator < Jekyll::Generator
    def generate(site)
      script_dir = site.config['folders']['scripts']
      ipynb_dir = site.config['folders']['ipynb']
      # url = site.config['url']

      script = script_dir + 'ipynb_to_jekyll.py'
      site.posts.each do |post|
        if post.ext =~ /^\.ipy$/
          ipynb = ipynb_dir + post.name.sub('.ipy', '.ipynb')
          content = `python #{script} #{ipynb}`
          # link = url + '/' + ipynb
          link = '../../' + ipynb

          post.content = '(Download this IPython Notebook [here](%s).)' % link
          post.content += '<br/>'
          post.content += content
          post.ext = '.md'
        end
      end
    end
  end
end
