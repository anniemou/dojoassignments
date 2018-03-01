$(document).ready(function(){
    
});

$(document).ready(function(){

    $('#hide .button').click(function(){
        $('#hide .p').hide();
    })

  $('#show .button').click(function(){
          $('#show .p').show();
      })

  $('#toggle .button').click(function(){
          $('#toggle .p').toggle();
      })
  $('#slideDown .button').click(function(){
          $('#slideDown .p').slideDown();
      })
  $('#slideUp .button').click(function(){
          $('#slideUp .p').slideUp();
      })
  $('#slideToggle .button').click(function(){
          $('#slideToggle .p').slideToggle();
      })
  $('#faleIn .button').click(function(){
          $('#faleIn .p').fadeIn();
      })   
  $('#fadeOut .button').click(function(){
          $('#fadeOut .p').fadeOut();
      })

      // 
  $('#addClass .button').click(function(){
          $('#addClass .p').addClass('blue');
      })    
  $('#before .button').click(function(){
          $('#before .p').before('<div>This is inserted before the P tag</div>');
      })
  $('#after .button').click(function(){
          $('#after .p').after('<div>This is inserted after the P tag</div>');
      })   
  $('#append .button').click(function(){
          $('#append .h1').append('This is appended to the end of the p');
      })  
  $('#html .button').click(function(){
          var html = $('#html .p').html();
          $("#html .p").append(html);
      })
  $('#attr .button').click(function(){
          var red = $('#attr .p').attr('id');
          $('#attr .h1').addClass(red);
      })  
  $('#val .button').click(function(){
          var fruit = $('#val select').val();
          $('#val .p').append(fruit);
      })   
  $('#text .button').click(function(){
          var text = $('#text .p').text();
          $('#text .p').append(text);
      })      
    $('#data .button').click(function () {
        var data = $('#data .p').data('data', { first: 'banana', second: "apple" });
        $('#data .p').text($('#data .p').data('data').second);
    })

})
