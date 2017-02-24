$(document).ready(function () {
    $.fn.extend({
        popup:function(content,position){
            $(this).popover({
                trigger:'manual',
                placement:position,
                content:content,
            });
            $(this).popover('show');
            var that = this;
            setTimeout(function(){
                $(that).popover('destroy');
            },2000);
        }
    });
});
