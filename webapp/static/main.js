$(document).ready(function() {
    function predict(text, number) {
        $.ajax({
            url: '/predicio',
            type: 'POST',
            data: {
                'text': text,
                'number': number
            },
            success: function(data) {
                $('#predicted-text-box').css('background-color', '#66bb6a');
                $('#predicted-text-box').html(data);
            }
        });
    };

    $('#predict-btn').click(function() {
        var text = $('#text-box').val();
        var number = $('#number-box').val();
        predict(text, number);
    });
});
