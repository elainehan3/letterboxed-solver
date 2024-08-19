$(document).ready(function() {

  $('#autoPopulate').click(function(){

    console.log("hello");

    $.ajax({
      url: "/populate",
      type: "get",
      success: function(res) {

        $('#leftInput').val(res[3]);
        $('#topInput').val(res[0]);
        $('#rightInput').val(res[1]);
        $('#bottomInput').val(res[2]);
     
      }
    });

  });

   $('#retrieve').click(function(){

     setupCanvas(canvasIn)
     setupCanvas(canvasOut)
     $('.pattern').css('background-image','');

     $('.error').html('');
     $('.loader').show();

       var l = $('#leftInput').val();
       var t = $('#topInput').val();
       var r = $('#rightInput').val();
       var b = $('#bottomInput').val();
       var num = $('input[name=num]:checked').val();

       // empty div with new request
       $('#results').html('<div></div>');

       $.ajax({
         url: "/transform",
         type: "get",
         data: {left: l, top: t, right: r, bottom: b, number: num},
         success: function(response) {

           // Input error
           if (response.html == 'Please input 3 distinct letters per side!') {
             $('.loader').hide();
             $('.error').html(response.html);
           }
           // No easy solutions found
           else if (response.html.includes('-word solutions found!')) {

             // Look for hard solution
             $.ajax({
               url: "/transform_hard",
               type: "get",
               data: {left: l, top: t, right: r, bottom: b, number: num},
               success: function(res) {

                 $('.loader').hide();

                 if (res.html.includes('-word solutions found!')) {
                   // No solutions found
                   $('.error').html(res.html);
                 }
                 else {
                   // Hard solution only
                   $('.pattern').css('background-image', 'url(static/reveal.png)');
                   $("#results").show();
                   $("#results").html(res.html);
                   $("#results").prepend("<strong><ul>Try these answers!</ul></strong><p>");
                 }
               }
             });
           }
           // Easy solution found
           else {

             $('.loader').hide();
             $('.pattern').css('background-image', 'url(static/reveal.png)');
             $("#results").show();
             $("#results").html(response.html);
             $("#results").prepend("<strong><ul>Try these answers!</ul></strong><p>");

             // Looking for additional hard solutions
             $('#results').append("<div class='find'><strong><ul>Looking for more answers using less common words...<div class='find-loader'><img src='static/ajax-loader.gif'></img></div></ul></strong><p></div>");
             $.ajax({
               url: "/transform_hard",
               type: "get",
               data: {left: l, top: t, right: r, bottom: b, number: num},
               success: function(res) {

                 $(".find").hide();

                 if (res.html.includes('-word solutions found!')) {
                   // No additional hard solutions found -- display text?
                 }
                 else {
                   // Additional hard solution found
                   $("#results").append("<strong><ul>Check out these additional answers using less common words!</ul></strong><p>");
                   $('#results').append(res.html);
                 }

               }
             });

          }
        },
        error: function(xhr) {
          //Do Something to handle error
     }
     });
   });

 });
