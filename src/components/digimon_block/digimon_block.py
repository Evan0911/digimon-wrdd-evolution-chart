from django_components import component
from interfaces.digimon_data import digimonData

@component.register("digimonBlock")
class DigimonBlock(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found. To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "digimon_block/digimon_block.html"
    
    
    def get_context_data(self):
      return {
        "tailmon": digimonData("Gatomon", "Tailmon", ["Angewomon", "Holydramon"], ["Plotmon"], 0, 1000, 0, 80, 0, 60, 10, 0, 0, 1, 0, 0, 0, 0, 15, 0, 14, 7, 3)

      }

    class Media:
        css = "digimon_block/digimon_block.css"
        js = "digimon_block/digimon_block.js"