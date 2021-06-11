Ir em templates (Section_5_Django_Framework_avancado\Projeto\core\templates):

404.html:

```html

{% extends 'base.html' %}
{% load i18n %} # <--- adicionar load i18n

{% block content %}

{% load static %}

<div id="hero-area" class="hero-area-bg">
    <div class="container">
      <div class="row">
        <div class="col-lg-7 col-md-12 col-sm-12 col-xs-12">
          <div class="contents">
            <h2 class="head-title">404<br>{% trans 'Página não encontrada' %}</h2> <--- adicionar nos textos {% trans 'msg' %}
            <p>{% trans 'Infelizmente a página que você procura não está disponível' %}</p>
            <div class="header-button">
              <a href="{% url 'index' %}" class="btn btn-common">{% trans 'Voltar para página inicial' %}</i></a>
            </div>
          </div>
        </div>
        <div class="col-lg-5 col-md-12 col-sm-12 col-xs-12">
          <div class="intro-img">
            <img class="img-fluid" src="{% static 'img/intro-mobile.png' %}" alt="">
          </div>
        </div>
      </div>
    </div>
  </div>
</header>

{% endblock %}

```

500.html

```html

{% extends 'base.html' %}
{% load i18n %}
{% block content %}

{% load static %}

<div id="hero-area" class="hero-area-bg">
    <div class="container">
      <div class="row">
        <div class="col-lg-7 col-md-12 col-sm-12 col-xs-12">
          <div class="contents">
            <h2 class="head-title">500<br>{% trans 'Erro de processamento' %}</h2>
            <p>Infelizmente não foi possível processar sua requisição</p>
            <div class="header-button">
              <a href="{% url 'index' %}" class="btn btn-common">{% trans 'Voltar para página inicial' %}</i></a>
            </div>
          </div>
        </div>
        <div class="col-lg-5 col-md-12 col-sm-12 col-xs-12">
          <div class="intro-img">
            <img class="img-fluid" src="{% static 'img/intro-mobile.png' %}" alt="">
          </div>
        </div>
      </div>
    </div>
  </div>
</header>

{% endblock %}

```

base.html:

```html
{% load static %}
{% load i18n %}
<!DOCTYPE html>
<html lang="{{ lang }}">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <title>Fusion</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}" >
    <!-- Icon -->
    <link rel="stylesheet" href="{% static 'fonts/line-icons.css' %}">
    <!-- Owl carousel -->
    <link rel="stylesheet" href="{% static 'css/owl.carousel.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/owl.theme.css' %}">

    <!-- Animate -->
    <link rel="stylesheet" href="{% static 'css/animate.css' %}">
    <!-- Main Style -->
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
    <!-- Responsive Style -->
    <link rel="stylesheet" href="{% static 'css/responsive.css' %}">

  </head>
  <body>

    <!-- Header Area wrapper Starts -->
    <header id="header-wrap">
      <!-- Navbar Start -->
      <nav class="navbar navbar-expand-md bg-inverse fixed-top scrolling-navbar">
        <div class="container">
          <!-- Brand and toggle get grouped for better mobile display -->
          <a href="{% url 'index' %}" class="navbar-brand"><img src="{% static 'img/logo.png' %}" alt=""></a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <i class="lni-menu"></i>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav mr-auto w-100 justify-content-end clearfix">
              <li class="nav-item active"> 
                <a class="nav-link" href="#hero-area">
                  {% trans 'Home' %}
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#services">
                  {% trans 'Services' %}
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#team">
                  {% trans 'Team' %}
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#pricing">
                  {% trans 'Pricing' %}
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#testimonial">
                  {% trans 'Testimonial' %}
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#contact">
                  {% trans 'Contact' %}
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <!-- Navbar End -->

    {% block content %} {% endblock %}

    <!-- Go to Top Link -->
    <a href="#" class="back-to-top">
    	<i class="lni-arrow-up"></i>
    </a>

    <!-- Preloader -->
    <div id="preloader">
      <div class="loader" id="loader-1"></div>
    </div>
    <!-- End Preloader -->

    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="{% static 'js/jquery-min.js' %}"></script>
    <script src="{% static 'js/popper.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
    <script src="{% static 'js/owl.carousel.min.js' %}"></script>
    <script src="{% static 'js/wow.js' %}"></script>
    <script src="{% static 'js/jquery.nav.js' %}"></script>
    <script src="{% static 'js/scrolling-nav.js' %}"></script>
    <script src="{% static 'js/jquery.easing.min.js' %}"></script>  
    <script src="{% static 'js/main.js' %}"></script>
    <script src="{% static 'js/form-validator.min.js' %}"></script>
    <script src="{% static 'js/contact-form-script.min.js' %}"></script>

  </body>
</html>

```

Devido a modificação acima, deve novamente digitar o comando:

```bash
\$ python manage.py makemessages -l it -i "venv"
processing locale it
(venv)

$ python manage.py compilemessages -i 'venv'
processing file django.po in C:\\Users\\jamal_ghatit\\Documents\\GitHub\\Django_udemy\\Section_5_Django_Framework_avancado\\Projeto\\locale\\it\\LC_MESSAGES
(venv)

```