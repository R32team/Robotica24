<?xml version="1.0" encoding="UTF-8" ?>
<Package name="face tracker" format_version="5">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
        <Dialog name="variabili" src="variabili/variabili.dlg" />
        <Dialog name="d1" src="d1/d1.dlg" />
        <Dialog name="domanda" src="domanda/domanda.dlg" />
    </Dialogs>
    <Resources />
    <Topics>
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" nuance="enu" />
        <Topic name="variabili_iti" src="variabili/variabili_iti.top" topicName="variabili" language="it_IT" nuance="iti" />
        <Topic name="d1_iti" src="d1/d1_iti.top" topicName="d1" language="it_IT" nuance="iti" />
        <Topic name="domanda_iti" src="domanda/domanda_iti.top" topicName="domanda" language="it_IT" nuance="iti" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="it_IT">
        <Translation name="translation_it_IT" src="translations/translation_it_IT.ts" language="it_IT" />
    </Translations>
</Package>
