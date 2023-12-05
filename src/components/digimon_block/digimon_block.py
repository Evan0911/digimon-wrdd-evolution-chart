from django_components import component

@component.register("digimonBlock")
class DigimonBlock(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found. To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "digimon_block/digimon_block.html"

    class Media:
        css = "digimon_block/digimon_block.css"
        js = "digimon_block/digimon_block.js"