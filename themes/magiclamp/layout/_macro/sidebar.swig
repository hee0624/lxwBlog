{% macro render(is_post) %}
  <div class="sidebar-toggle">
    <div class="sidebar-toggle-line-wrap">
      <span class="sidebar-toggle-line sidebar-toggle-line-first"></span>
      <span class="sidebar-toggle-line sidebar-toggle-line-middle"></span>
      <span class="sidebar-toggle-line sidebar-toggle-line-last"></span>
    </div>
  </div>

  <aside id="sidebar" class="sidebar">
    <div class="sidebar-inner">
      {% if is_post %}
        <ul class="sidebar-nav motion-element">
          <li class="sidebar-nav-toc sidebar-nav-active" data-target="post-toc-wrap" >
            {{ __('sidebar.toc') }}
          </li>
          <li class="sidebar-nav-overview" data-target="site-overview">
            {{ __('sidebar.overview') }}
          </li>
        </ul>
      {% endif %}

      <section class="site-overview">
        <div class="site-author motion-element" itemprop="author" itemscope itemtype="http://schema.org/Person">
          <img class="site-author-image" src="{{ theme.avatar or url_for(theme.images) + '/lxwAvatar.png' }}" alt="{{ theme.author }}" itemprop="image"/>
          <p class="site-author-name" itemprop="name">{{ theme.author }}</p>
        </div>
        <p class="site-description motion-element" itemprop="description">{{ theme.description }}</p>
        <nav class="site-state motion-element">
          <div class="site-state-item site-state-posts">
            <a href="{{ url_for(theme.menu.archives) }}">
              <span class="site-state-item-count">{{ site.posts.length }}</span>
              <span class="site-state-item-name">{{ __('state.posts') }}</span>
            </a>
          </div>

          <div class="site-state-item site-state-categories">
            {% if theme.menu.categories %}<a href="{{ url_for(theme.menu.categories) }}">{% endif %}
              <span class="site-state-item-count">{{ site.categories.length }}</span>
              <span class="site-state-item-name">{{ __('state.categories') }}</span>
              {% if theme.menu.categories %}</a>{% endif %}
          </div>

          <div class="site-state-item site-state-tags">
            {% if theme.menu.tags %}<a href="{{ url_for(theme.menu.tags) }}">{% endif %}
              <span class="site-state-item-count">{{ site.tags.length }}</span>
              <span class="site-state-item-name">{{ __('state.tags') }}</span>
              {% if theme.menu.tags %}</a>{% endif %}
          </div>

        </nav>

        {% if theme.rss %}
          <div class="feed-link motion-element">
            <a href="{{ url_for(theme.rss) }}" rel="alternate">

              <i class="menu-item-icon icon-next-feed"></i>
              RSS
            </a>
          </div>
        {% endif %}

        <!-- lxw
        <div class="links-of-author motion-element">
          {% if theme.social %}
            {% for name, link in theme.social %}
              <span class="links-of-author-item">
                <a href="{{ link }}" target="_blank">{{ name }}</a>
              </span>
            {% endfor %}
          {% endif %}
        </div>
        -->

        <div class="links-of-author motion-element">
          <span class="links-of-author-item">
            <a href="https://github.com/lxw0109" target="_blank">
                <i class="fa fa-github fa-2x"></i>
            </a>
            <a href="http://weibo.com/xiaopeien" target="_blank">
                <i class="fa fa-weibo fa-2x"></i>
            </a>
            <a href="http://stackoverflow.com/users/3374961/lxw" target="_blank">
                <i class="fa fa-stack-overflow fa-2x"></i>
            </a>
            <a href="mailto:liu_xiaowei@foxmail.com" target="_blank">
                <i class="fa fa-envelope fa-2x"></i>
            </a>
            <!--
            <a href="https://plus.google.com/u/0/117086975269574756424" target="_blank">
                <i class="fa fa-google-plus fa-2x"></i>
            </a> -->
          </span>
        </div>

        <div class="links-of-friendly motion-element">
          {% if theme.links %}
            <p class="site-author-name">{{ theme.links_title }}</p>
            {% for name, link in theme.links %}
              <span class="links-of-author-item">
              <a href="{{ link }}" target="_blank">{{ name }}</a>
              </span>
            {% endfor %}
          {% endif %}
        </div>

        {% set cc = {'by': 1, 'by-nc': 1, 'by-nc-nd': 1, 'by-nc-sa': 1, 'by-nd': 1, 'by-sa': 1, 'zero': 1} %}
        {% if theme.creative_commons in cc %}
          <div class="cc-license motion-element" itemprop="license">
            <a href="http://creativecommons.org/licenses/{{ theme.creative_commons }}/4.0" class="cc-opacity" target="_blank">
              <img src="{{ url_for(theme.images) }}/cc-{{ theme.creative_commons }}.svg" alt="Creative Commons" />
            </a>
          </div>
        {% endif %}

      </section>

      {% if is_post %}
        <section class="post-toc-wrap sidebar-panel-active">
          <div class="post-toc-indicator-top post-toc-indicator"></div>
          <div class="post-toc">
            {% set toc = toc(page.content, {"class": "nav", list_number: theme.toc_list_number}) %}
            {% if toc.length <= 1 %}
              <p class="post-toc-empty">{{ __('post.toc_empty') }}</p>
            {% else %}
              <div class="post-toc-content">{{ toc }}</div>
            {% endif %}
          </div>
          <div class="post-toc-indicator-bottom post-toc-indicator"></div>
        </section>
      {% endif %}

    </div>
    <a href="https://github.com/lxw0109"><img style="position: absolute; top: -1px; right: -1px; border: 0;" src="/images/forkme.png" alt="Fork me on GitHub"></a>
  </aside>
{% endmacro %}
