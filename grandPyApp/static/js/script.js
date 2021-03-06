$(document).ready(function(){ 

  // Mapbox
  function mapbox(data) {
    mapboxgl.accessToken = $ACCESS_TOKEN; 
    var map = new mapboxgl.Map({
      container: 'mapbox',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: data['geo_coord_results'], // [-0.50, 44.80], // starting position [lng, lat]
      zoom: 9 // starting zoom
    });
    var marker = new mapboxgl.Marker({color: '#40834f'})
    .setLngLat(data['geo_coord_results'])
    .addTo(map);
  };

  // Fill "dialog" with input text and scroll down in div
  function insertDialog(data) {    
    let $list = $('.messages');
    // Modify template
    $('#message_template .text1').html(data['answer']);
    $('#message_template .text2').html(data['bonus_message']);
    $('#message_template .text3').html("<b>L'adresse est : </b>" + data['geo_adress_results']);
    $('#message_template .text4').html("<b>Saviez-vous que : </b>" + data['wiki_results']);
    // If fail : change border color to red
    if (data['geo_fail'] === true)
      $('#message_template .text_wrapper3').addClass('wrapper_border_red').removeClass('wrapper_border_green');
    if (data['wiki_fail'] === true)
      $('#message_template .text_wrapper4').addClass('wrapper_border_red').removeClass('wrapper_border_green');
    // Apply template
    $($('#message_template').clone().html()).appendTo($list);
    // In dialog zone : scroll to bottom
    $('#dialog').scrollTop($('#dialog')[0].scrollHeight);
    // Reset borders colors
    $('#message_template .text_wrapper3').addClass('wrapper_border_green').removeClass('wrapper_border_red');
    $('#message_template .text_wrapper4').addClass('wrapper_border_green').removeClass('wrapper_border_red');
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
    // Scroll bottom to show loading gif
    $('#dialog').scrollTop($('#dialog')[0].scrollHeight);
    // Hide fail_box
    $('#fail_box').hide();
    // Clean fail_text
    $('#fail_text').empty(); 
  }

  function postDone(data){
    // Return results in "dialog" zone.
    insertDialog(data);
    // Clean input form and disable send button  
    $('#question input:text').val(''); 
    $('#sendBtn').attr("disabled",true);
    // Display and refresh map position with coordinates.
    $('#jb_map').show("slow");
    mapbox(data);
    // Hide loading gif   
    $('#loading_gif').hide();
  };

  function postFail(){
    // Display fail box and add message.
    $('#fail_box').show("slow");
    $('#fail_text').append('Requête échouée !'); // TC
    // Hide loading gif
    $('#loading_gif').hide();  
  };

  // Scroll bottom when resize
  $(window).resize(function(){
    $('#dialog').scrollTop($('#dialog')[0].scrollHeight);
  });

  // Scrollspy smooth
  $(function(){
    $('header a').on('click', function(e) {
      e.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(this.hash).offset().top-60
      }, 1000, function(){
        // window.location.hash = hash;
      });
    });
  });
});