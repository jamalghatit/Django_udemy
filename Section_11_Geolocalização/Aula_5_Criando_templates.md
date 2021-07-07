# Criando os templates

Criar arquivo base.html (Section_11_Geolocalização\geo\core\templates\base.html):

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">

        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css">
        <script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js"></script>

        <title>Geek busca</title>

        <style>
            .gmap{
                height: 400px;
                width: 100%;
            }
        </style>
    </head>

    <body>
        <div class="container">
            {% block content %} {% endblock %}
        </div>

        <script src="https://code.jquery.com/jquery-3.3.1.slim.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
    </body>

</html>
```

Criar arquivo index.html (Section_11_Geolocalização\geo\core\templates\index.html):

```html
{% extends 'base.html' %}

{% block content %}
    <div class="row">
        <div class="col-sm-6">
            <form autocomplete="off" action="{% url 'index' %}">
                {% csrf_token %}
                <div class="form-group">
                    <h1><a href="{% url 'index' %}">Buscador Geek</a></h1>
                    <h4>[{{ city }} {% if country %} - {{ country }} {% endif %}]</h4>
                </div>
                <div class="form-group">
                    <input class="form-control" type="text" name="key" placeholder="Digite um termo para busca (obrigatório)" required/>
                    <small id="keyHelp" class="form-text text-muted">Exemplo: Mexican Food, Brazilian Food, Asian Food</small>
                </div>
                <div class="form-group">
                    <input class="form-control" type="text" name="loc" placeholder="Digite uma cidade para efetuar a busca"/>
                    <small id="keyLoc" class="form-text text-muted">Exemplo: Vancouver, Madrid, Mexico City</small>
                </div>
                <button type="submit" class="btn btn-primary">Buscar</button>
            </form>
            {% if 'error' in items %}
                <h1>Nenhum estabelecimento encontrado em {{ city }}</h1>
            {% elif busca and items.businesses|length < 1 %}
                <h1>Nada encontrado sobre o termo buscado</h1>
            {% elif city and items %}
                <h1>Resultado da Busca</h1>
                {% for biz in items.businesses %}
                    <span class="text-info">{{ biz.name }}, {{ city }}</span><br/>
                {% endfor %}
            {% endif %}
        </div>
        {% if city and items|length > 1 %}
            {% include 'maps.html' %}
        {% endif %}
{% endblock %}

```

Criar arquivo maps.html (Section_11_Geolocalização\geo\core\templates\maps.html):

```html
<div class="col-sm-6">
    <h3 class="text-primary">Localidades</h3>
    <div id="mapDiv" class="gmap"></div>
</div>
</div>
<script>
    var lat = {{ items.businesses.0.coordinates.latitude | safe }};
    var lon = {{ items.businesses.0.coordinates.longitude | safe }};

    var map = L.map('mapDiv').setView([lat, lon], 13); //0 até 18

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
        maxZoom: 18,
    }).addTo(map);

    {% for biz in items.businesses %}
        var marker = L.marker([{{ biz.coordinates.latitude | safe}}, {{ biz.coordinates.longitude | safe}}]).addTo(map);

        marker.bindPopup("<b>{{ biz.name }}</b><br/>{{ biz.location.display_address.0 }} {{ biz.location.display_address.1 }}<br/>{{ city }}").openPopup();
    {% endfor %}


</script>
```

