$(function() {
    $(".dropdown-menu").on('click', 'li a', function(e) {
        e.preventDefault();
        $(".btn:first-child").text($(this).text());
        $(".btn:first-child").val($(this).text());
        if ($(this).attr("data-id").length > 0) {
            $('.fetch-trigger').removeAttr("disabled");
            $('.meta-info').removeClass('meta-info-off');
            $('.meta-info .services-list').text($(this).attr("data-services"));
            $('.meta-info .attributes-list').text($(this).attr("data-attributes"));
        }
   });
});