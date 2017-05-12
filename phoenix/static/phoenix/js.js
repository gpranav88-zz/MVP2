$(function() {
    $(".meta-info").on('click', '.crunch-trigger', function(e) {
        e.preventDefault();
        var static_media_path = "static/phoenix/";
        var rule_id = $(this).attr("data-id");
        $('#loading-image').show();
        $("#target").attr("src", "/phoenix/static/phoenix/bg.png");
        $("#target").attr("height", "300px");
        $("#target").attr("width", "300px");
        var x = setTimeout(function() {
            $('#loading-image').hide();
            $("#target").attr("src", static_media_path + "image" + rule_id + ".png");
            $("#target").attr("height", "80%");
            $("#target").attr("width", "80%");
        }, Math.floor(Math.random() * 1000) + 1000);
        $('#target').show();
        $(".trigger-link").attr("data-signal-id", rule_id);
   });
    var test_dump = '{WLF_MMB_11,LCC_DEL_38,WLF_MMB_04,WLF_MMB_10,CBP_AHM_02,MAG_CHN_10,MAM_HYD_17}';

    $(".csv-data").on('click', '#target', function(e) {
        e.preventDefault();
        $('.csv-dump').text(test_dump);
   });
});