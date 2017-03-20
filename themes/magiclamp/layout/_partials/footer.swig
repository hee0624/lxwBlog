<div class="theme-info">
  {% set current = date(Date.now(), "YYYY") %}
  &copy; {% if theme.since and theme.since != current %} {{ theme.since }} - {% endif %}
  <span itemprop="copyrightYear"> {{ current }} </span>
  <span class="author" itemprop="copyrightHolder">{{ config.author }}
  </span>
  {% if (theme.busuanzi) %}
    <span>&nbsp;|&nbsp;{% include '../_scripts/analytics/busuanzi.swig' %} </span>
  {% endif %}
  &nbsp;|&nbsp;Powered by <a class="theme-link" href="http://hexo.io">Hexo</a>
  &nbsp;|&nbsp;Theme by <a class="theme-link" href="http://blog.idhyt.com">idhyt</a>.<a class="theme-link" href="https://github.com/idhyt/hexo-theme-next/tree/magiclamp">{{ theme.scheme }}</a>
</div>
{% block footer %}{% endblock %}
