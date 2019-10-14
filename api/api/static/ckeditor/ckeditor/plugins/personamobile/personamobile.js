CKEDITOR.plugins.add('personamobile', {
    icons: 'personamobile',
    init: function (editor) {
        console.log("qweqweqwe")
    }
});

CKEDITOR.on('dialogDefinition', function (ev) {
    var dialogName = ev.data.name;
    var dialogDefinition = ev.data.definition;
    console.log(dialogDefinition)

    if (dialogName == 'image') {
        var infoTab = dialogDefinition.getContents('info');
        console.log(infoTab)
        infoTab.remove('txtBorder'); //Remove Element Border From Tab Info
        infoTab.remove('txtHSpace'); //Remove Element Horizontal Space From Tab Info
        infoTab.remove('txtVSpace'); //Remove Element Vertical Space From Tab Info
        infoTab.remove('txtWidth'); //Remove Element Width From Tab Info
        infoTab.remove('txtHeight'); //Remove Element Height From Tab Info
        infoTab.remove('htmlPreview'); //Remove Element Height From Tab Info
        infoTab.remove(2); //Remove Element Height From Tab Info
        infoTab.remove('cmbAlign'); //Remove Element Height From Tab Info
        infoTab.remove('ratioLock'); //Remove Element Height From Tab Info
        console.log(infoTab)

        //Remove tab Link
        dialogDefinition.removeContents('Link');
        dialogDefinition.removeContents('advanced');
        console.log(dialogDefinition)
    }
});