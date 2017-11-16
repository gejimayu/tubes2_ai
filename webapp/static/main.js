$(document).ready(function() {
    $('#predict-btn').click(function() {
        var age = $('#age-input').val();
        var workclass = $('#workclass-input').val();
        var education = $('#education-input').val();
        var education_number = $('#education-number-input').val();
        var marital_status = $('#marital-status-input').val();
        var occupation = $('#occupation-input').val();
        var relationship = $('#relationship-input').val();
        var race = $('#race-input').val();
        var sex = $('#sex-input').val();
        var capital_gain = $('#capital-gain-input').val();
        var capital_loss = $('#capital-loss-input').val();
        var hours_per_week = $('#hours-per-week-input').val();
        var native_country = $('#native-country-input').val();

        var empty = false;
        $('input[type="number"]').each(function() {
            if ($(this).val() == "") {
                empty = true;
            }
        });

        if (empty) {
            alert("Please fill in all fields");
        } else {
            $.ajax({
                url: '/predict',
                type: 'POST',
                data: {
                    'age': age,
                    'workclass': workclass,
                    'education': education,
                    'education_number': education_number,
                    'marital_status': marital_status,
                    'occupation': occupation,
                    'relationship': relationship,
                    'race': race,
                    'sex': sex,
                    'capital_gain': capital_gain,
                    'capital_loss': capital_loss,
                    'hours_per_week': hours_per_week,
                    'native_country': native_country
                },
                success: function(data) {
                    $('#predicted-text-box').css('background-color', '#2196f3');
                    $('#predicted-text-box').html(data);

                    $("html, body").animate({ scrollTop: $(document).height() }, 1000);
                }
            });
        }
    });
});
