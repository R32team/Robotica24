<?xml version="1.0" encoding="UTF-8" ?>
<Package name="face tracker" format_version="5">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
        <Dialog name="variabili" src="variabili/variabili.dlg" />
        <Dialog name="dialogo" src="dialogo/dialogo.dlg" />
    </Dialogs>
    <Resources />
    <Topics>
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" nuance="enu" />
        <Topic name="variabili_iti" src="variabili/variabili_iti.top" topicName="variabili" language="it_IT" nuance="iti" />
        <Topic name="dialogo_iti" src="dialogo/dialogo_iti.top" topicName="dialogo" language="it_IT" nuance="iti" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="it_IT">
        <Translation name="translation_it_IT" src="translations/translation_it_IT.ts" language="it_IT" />
    </Translations>
</Package>
