
var DLISTS = (function() {
    
    function initListeners() {
        $('.dlists-edit').click(function() {
            toggleEdit($(this).attr('data'));
        });
        $('.dlists-delete').click(function() {
            deleteLink($(this).attr('data'));
        });

        $("#sortable").sortable({
            revert: true,
            stop: saveWeights
        });
        $("#sortable section").disableSelection();
    }

    function toggleEdit(pk) {
        $('.link-container' + pk).toggleClass('hide');
        $('.form' + pk).toggleClass('hide');
    }

    function deleteLink(formName) {
        if (confirm('Are you sure?')) {
            $('form[name=' + formName + ']').submit();
        }
    }

    function saveWeights() {
        var i,
            arrayIds = [],
            arrayElements = $('section.sortable');
        for (i = 0; i < arrayElements.length; i++) {
            arrayIds.push($(arrayElements[i]).attr("id"));
        }
        $.post('/_ajax/update_weights/',
            {
                'ids': JSON.stringify(arrayIds)
            }
        );
    }

    return {
        initListeners: initListeners
    }
})();

$(document).ready(function() {
    DLISTS.initListeners();
});

jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});