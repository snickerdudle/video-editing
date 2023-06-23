from dataclasses import dataclass
from typing import List, Optional


class Prompt:
    def __init__(
        self,
        prompt_template: str,
        aux_text: Optional[List[str]] = None,
        input_text: Optional[str] = "",
    ):
        self.prompt_template = prompt_template
        self.aux_text = aux_text or []
        self.input_text = input_text

    def assemblePrompt(self, input_text: str = "") -> str:
        self.input_text = input_text if input_text else self.input_text
        return self.prompt_template.format(self=self)


summarization_prompt_1 = (
    "Below is a transcript of a video without any "
    "timestamps. Analyze the content of the video, and create a "
    "detailed section-by-section breakdown of the progression of the video and the "
    "topics discussed. Organize the sections hierarchically, grouping individual "
    "events into larger themes, then into larger ones, and on and on until you've "
    "grouped everything into the overarching video group. Instead of creating long, "
    "comma-separated descriptions, bias towards listing the same elements as sub-"
    "items of the current item. Return the analysis in the form of an indented list, "
    "imitating the formatting of this example:\n"
    "{self.aux_text[0]}\n\n"
    "VIDEO TRANSCRIPT:\n{self.input_text}"
)
summarization_example_1 = """-Video
--Intro
---Describing the adventure
----The narrator provides an overview of the upcoming adventure, setting the stage for the thrilling journey ahead.
--Team Explores
---Discovering the unknown
----The adventurers exploring mysterious landscapes and encountering breathtaking sights.
---Uncovering hidden treasures
----They stumble upon hidden clues, solve intricate puzzles, and unearth valuable artifacts.
--Difficulties ensue
---Overcoming obstacles
----The team faces treacherous terrains, tricky riddles, and physical tests of strength and skill.
---Facing dangerous creatures
----They encounter fierce creatures guarding the path to their goal.
-----Gorgoyles
-----Mutants
-----Giant spiders
-----Venomous snakes
--Coming out on top
---Epic battle
----The adventurers face a formidable enemy or group of adversaries.
-----Enemy is scared of sunlight
-----Enemy is allergic to silver
---Revealing the ultimate secret
----The adventurers discover the long-guarded secret that holds immense power or knowledge.
-----The secret to eternal life
-----The secret to unlimited wealth
-----The secret to ultimate power"""

video_summarization_prompt = Prompt(
    prompt_template=summarization_prompt_1, aux_text=[summarization_example_1]
)