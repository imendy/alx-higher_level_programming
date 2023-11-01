$(document).ready(function(){
    $.getJSON('https://swapi-api.hbtn.io/api/people/5/?', {format: 'json'}, function(data, textStatus){
    $('#character').append(data.name);
})
})
