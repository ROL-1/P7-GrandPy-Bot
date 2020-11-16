// $.(document).ready(function(){ 

// Mapbox
function mapbox(data) {
  mapboxgl.accessToken = 'pk.eyJ1Ijoicm9sLTEiLCJhIjoiY2tncnhvOHZtMGpleTJ4cXdrenN0aGMzYSJ9.DikocYiTLvwfLSvHwD42Hw';
  var map = new mapboxgl.Map({
    container: 'mapbox',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: data['geo_coord_results'], // [-0.50, 44.80], // starting position [lng, lat]
    zoom: 9 // starting zoom
  });
  var marker = new mapboxgl.Marker()
    .setLngLat(data['geo_coord_results'])
    .addTo(map);
};

// Fill "dialog" with input text
function insertDialog(data) {
  let $list;
  $list = $('#dialog ul');
  $list.append('<li>' + "Votre question : " + data['answer'] + '</li>');
  // $list.append('<li>' + data['geo_coord_results'] + '</li>');
  $list.append('<li>' + "L'adresse est la suivante : " + data['geo_adress_results'] + '</li>');
  $list.append('<li>' + "Et pour votre information : " + data['wiki_results'] + '</li></br>');  
};

// Submit form on Enter key press
$('#question').keypress((e) => { 
  if (this.which === 13) { 
    $('#question').submit(); 
  };
});

// Enable submit button if input is not empty
$("#userquestion").on('keyup', function(){
  if($(this).val().length !=0)
    $('#sendBtn').attr("disabled",false);
  else
    $('#sendBtn').attr("disabled",true);
});


// Listen Form send and use POST request
$('#question').on('submit', function(e) {
  e.preventDefault();
  postStart();
  $.post(
    '/api/getAnswer',
    {question : $('#question input:text').val(), 
    },
  )
  .done(function(data){
    postDone(data);
  })
  .fail(function(){
    postFail();
  })
}); 

function postStart(){
  // Display loading gif
  $('#loading_gif').show(); 
  // Hide fail_box
  $('#fail_box').hide();
  // Clean fail_text
  $('#fail_text').empty(); 
}

function postDone(data){
  // Return results in "dialog" zone.
  insertDialog(data);
  // Clean input form   
  $('#question input:text').val(''); 
  // Display and refresh map position with coordinates.
  $('#jb_map').show("slow");
  mapbox(data);
  // Hide loading gif   
  $('#loading_gif').hide();
};

function postFail(){
  // Display fail box and add message.
  $('#fail_box').show("slow");
  $('#fail_text').append('Requête échouée !'); 
  // Hide loading gif
  $('#loading_gif').hide();  
};

// Scrollspy smooth
$(function () {
  $('header a').on('click', function(e) {
    e.preventDefault();
    var hash = this.hash;
    $('html, body').animate({
      scrollTop: $(this.hash).offset().top
    }, 1000, function(){
      window.location.hash = hash;
    });
  });
});
