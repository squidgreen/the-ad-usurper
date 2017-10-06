$(document).ready(function() {

  $('form').submit(function(event) {

    var formData = {
      'zipcode' : $('input[name=zipcode]').val()
    };

    $.ajax({
      type      : 'GET',
      url       : 'handle_zip.py',
      data      : formData,
      dataType  : 'text',
      encode    : true
    })

      .done(function(data) {
        console.log(data);
      });

    event.preventDefault();
  });

});
