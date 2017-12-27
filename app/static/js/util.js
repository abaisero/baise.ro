// replace a tag;  from https://stackoverflow.com/a/24395071
$.extend({
    replaceTag: function (element, tagName, withDataAndEvents, deepWithDataAndEvents) {
        var newTag = $('<' + tagName + '>')[0];
        // From [Stackoverflow: Copy all Attributes](http://stackoverflow.com/a/6753486/2096729)
        $.each(element.attributes, function() {
            newTag.setAttribute(this.name, this.value);
        });
        // BAIS - children does not copy text
        // $(element).children().clone(withDataAndEvents, deepWithDataAndEvents).appendTo(newTag);
        $(element).contents().clone(withDataAndEvents, deepWithDataAndEvents).appendTo(newTag);
        return newTag;
    }
})
$.fn.extend({
    replaceTag: function (tagName, withDataAndEvents, deepWithDataAndEvents) {
        // Use map to reconstruct the selector with newly created elements
        return this.map(function() {
            return jQuery.replaceTag(this, tagName, withDataAndEvents, deepWithDataAndEvents);
        })
    }
})
