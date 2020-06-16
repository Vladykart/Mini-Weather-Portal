$(function () {

    var $city = $('#city').css('width', '250px').select2({
        minimumInputLength: 3,
          ajax: {
            width: 'resolve',
            url: 'http://gd.geobytes.com/AutoCompleteCity',
            dataType: "jsonp",
            data: function (params) {
              var query = {
                q: params.term
              }
              // Query parameters will be ?search=[term]&type=public
              return query;
            },
            processResults: function (data) {
              data = data.map(function (currentValue) {
                  return currentValue.split(',')[0];
              }).filter( function (value, index, self) {
                  return self.indexOf(value) === index;
              }).map(function (city) {
                  return {id: city, text: city};
              });
              return {results: data};
            }
          }
        });

    var $result = $('#city-weather');

    var $form = $('#city-form').on('submit', function(e) {
        e.preventDefault();
        $.post('', $form.serialize(), function (data) {
            console.log(data);
            $result.html(data);
        });
        return false;
    })

    $('.js-delete-city').on('click', function(e) {
        e.preventDefault();
        var $el = $(this);
        $.post('/delete-city', {
            id: $el.data('id'),
            csrfmiddlewaretoken: $('#csrf_token').prop('content')
        }, function (data) {
            if(data.success) {
                $el.closest('.box').remove();
            } else {
                alert(data.error || 'Error deleting city!');
            }
        });
        return false;
    })

    $('.select2-container').css("width","100%");

    $('#date_from, #date_to').datepicker({
        dateFormat: 'dd.mm.yyyy'
    });

});