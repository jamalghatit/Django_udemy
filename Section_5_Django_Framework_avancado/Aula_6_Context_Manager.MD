# Conhecendo e utilizando o Context Manager

Em 'Section_5_Django_Framework_avancado\Projeto\core\views.py':

```python

from django.views.generic import TemplateView

from .models import Service, Team

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all() # faz carregar conteudos aleatório
        context['team'] = Team.objects.order_by('?').all()
        return context

class TesteView(TemplateView):
    template_name = 'teste.html'

```

Ir no index.html e trabalhar em services.html e team.html:

```python

{% extends 'base.html' %}
{% load static %}
{% block content %}
    <!-- Hero Area Start -->
      {% include 'hero.html' %}
    <!-- Hero Area End -->

    <!-- Services Section Start -->
      {% include 'services.html' %}
    <!-- Services Section End -->

    <!-- About Section start -->
      {% include 'about.html' %}
    <!-- About Section End -->

    <!-- Features Section Start -->
      {% include 'features.html' %}
    <!-- Features Section End -->

    <!-- Team Section Start -->
      {% include 'team.html' %}
    <!-- Team Section End -->

    <!-- Pricing section Start -->
      {% include 'pricing.html' %}
    <!-- Pricing Table Section End -->

    <!-- Testimonial Section Start -->
      {% include 'testimonials.html' %}
    <!-- Testimonial Section End -->

    <!-- Call To Action Section Start -->
    {% include 'call.html' %}
    <!-- Call To Action Section Start -->

    <!-- Contact Section Start -->
    {% include 'contact.html' %}
    <!-- Contact Section End -->

    <!-- Footer Section Start -->
    {% include 'footer.html'%}
    <!-- Footer Section End -->

{% endblock %}

```


services.html:

```html

{% load static %}

<section id="services" class="section-padding">
    <div class="container">
      <div class="section-header text-center">
        <h2 class="section-title wow fadeInDown" data-wow-delay="0.3s">Our Services</h2>
        <div class="shape wow fadeInDown" data-wow-delay="0.3s"></div>
      </div>
      <div class="row">


        {% for service in services %}
        <!-- Services item -->
        <div class="col-md-6 col-lg-4 col-xs-12">
          <div class="services-item wow fadeInRight" data-wow-delay="0.3s">
            <div class="icon">
              <i class="{{ service.icon }}"></i>
            </div>
            <div class="services-content">
              <h3><a href="#">{{ service.services }}</a></h3>
              <p>{{ service.description }}</p>
            </div>
          </div>
        </div>
        <!-- Services item -->
        {% endfor %}

      </div>
    </div>
  </section>

```

team.html:

```python

{% for f in team %}
<div class="col-lg-6 col-md-12 col-xs-12">
    <!-- Team Item Starts -->
    <div class="team-item wow fadeInRight" data-wow-delay="0.2s">
    <div class="team-img">
        <img class="img-fluid" src="{{ f.image.thumbnail.url }}" alt=" {{ f.name }}">
    </div>
    <div class="contetn">
        <div class="info-text">
        <h3><a href="#">{{ f.name }}</a></h3>
        <p>{{ f.role }}</p>
        </div>
        <p>{{ f.bio }}</p>
        <ul class="social-icons">
        <li><a href="{{ f.facebook }}"><i class="lni-facebook-filled" aria-hidden="true"></i></a></li>
        <li><a href="{{ f.twitter }}"><i class="lni-twitter-filled" aria-hidden="true"></i></a></li>
        <li><a href="{{ f.instagram }}"><i class="lni-instagram-filled" aria-hidden="true"></i></a></li>
        </ul>
    </div>
    </div>
</div>
    <!-- Team Item Ends -->
    {% endfor %}

```