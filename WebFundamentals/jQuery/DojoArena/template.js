$(document).ready(function () {
    // JS and jQuery go here. 


    $('.location').hover(function (){
        
        var id = $(this).attr('id')
        
        $('#banner').attr('class', id);
    }, function (){

    })
    
    $('.location').on("click", function(){
        console.log('inside click');
        
        var id = $(this).attr('id')
        console.log(id);
        
        $('#banner').addClass('class');
        $('.select-arena').hide();
        $('.select-player').show();
    });

    $('#select_1').on('change', function(){
        console.log('inside select menu');
        var value = $(this).find(":selected").text();
        console.log(value);
        $('.player-one').show().addClass(value);
    });
    $('#select_2').on('change', function(){
        console.log('inside select menu');
        var value = $(this).find(":selected").text();
        console.log(value);
        $('.player-two').show().addClass(value);
    });

});