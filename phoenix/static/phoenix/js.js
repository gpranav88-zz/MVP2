$(function() {
    $(".meta-info").on('click', '.crunch-trigger', function(e) {
        e.preventDefault();
        var static_media_path = "static/phoenix/";
        var rule_id = $(this).attr("data-id");
        $('#loading-image').show();
        var x = setTimeout(function() {
            $('#loading-image').hide();
            $("#target").attr("src",static_media_path + "image"+rule_id+".jpg");
        }, 2000);
   });
});