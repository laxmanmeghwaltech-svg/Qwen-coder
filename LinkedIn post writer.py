#!/usr/bin/env python3
"""LinkedIn post + carousel script writer using CHEF and 70-20-10 mix."""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class BrandGuide:
    primary_background: str = "Dark Navy #0F172A"
    primary_structure: str = "Electric Blue #2563EB"
    secondary_text: str = "White #FFFFFF"
    secondary_annotation: str = "Muted Cool Gray #94A3B8"
    accent_cta: str = "Neon Cyan #22D3EE"
    header_font: str = "Montserrat or Space Grotesk"
    body_font: str = "Inter or Roboto"


class LinkedInPostWriter:
    """Creates LinkedIn post drafts and carousel scripts with clear structure."""

    def __init__(self, voice: str = "Direct, actionable, no filler") -> None:
        self.voice = voice
        self.brand = BrandGuide()

    def chef_framework(self) -> Dict[str, str]:
        return {
            "C": "Curate Context: Gather task context, tone, background data, rules, examples, conversation history, and immediate task before writing.",
            "H": "Heat with AI: Generate first drafts quickly from structured context.",
            "E": "Enhance with Flavour: Rewrite with your voice, specific opinions, and lived experience.",
            "F": "Feed the Community: Publish, reply to comments, and turn feedback into the next post.",
        }

    def content_mix(self, total_posts: int = 10) -> Dict[str, int]:
        teaching = round(total_posts * 0.7)
        proof = round(total_posts * 0.2)
        selling = total_posts - teaching - proof
        return {"teaching": teaching, "proof": proof, "selling": selling}

    def generate_post(self, topic: str, audience: str, offer: str) -> str:
        return f"""Hook:
Most creators don\'t have a content problem. They have a context problem.

Body:
If you want better LinkedIn output, use this 4-step CHEF system:

1) Curate Context
- Define the exact task for {audience}
- Set tone: {self.voice}
- Add background: links, proof, examples, and constraints

2) Heat with AI
- Ask for 3 first-draft angles on: {topic}
- Pick one and expand to a post + carousel outline

3) Enhance with Flavour
- Inject your POV, story, and specific examples
- Replace generic claims with concrete details

4) Feed the Community
- Publish
- Reply to comments within 24 hours
- Convert FAQs into next week\'s posts

CTA:
If you want help implementing this for {offer}, comment \"CHEF\" and I\'ll share a reusable prompt template."""

    def generate_carousel_script(self, topic: str) -> List[str]:
        return [
            f"Slide 1 (Headline, centered): The CHEF Framework for {topic}",
            "Slide 2 (left-aligned body): C = Curate Context: define task, tone, data, rules, and examples before drafting.",
            "Slide 3 (left-aligned body): H = Heat with AI: generate multiple draft angles fast, then pick the strongest one.",
            "Slide 4 (left-aligned body): E = Enhance with Flavour: add your story, proof, and sharp opinions.",
            "Slide 5 (left-aligned body): F = Feed the Community: publish, engage, and recycle comments into content.",
            "Slide 6 (left-aligned body): 70-20-10 mix: 70% teaching, 20% proof, 10% selling.",
            "Slide 7 (CTA with accent): Want the exact prompt template? Comment CHEF.",
        ]

    def design_guidelines(self) -> str:
        return f"""Design & Brand Guidelines
- Colors (60-30-10):
  - 60% background/primary: {self.brand.primary_background}, {self.brand.primary_structure}
  - 30% text/secondary: {self.brand.secondary_text}, {self.brand.secondary_annotation}
  - 10% accent/CTA: {self.brand.accent_cta} (keywords, arrows, final CTA only)
- Typography: max 2 fonts
  - Header: {self.brand.header_font}
  - Body: {self.brand.body_font}
- Alignment:
  - Center short headlines
  - Strictly left-align body text for scannability
"""


def main() -> None:
    writer = LinkedInPostWriter()

    topic = "creating LinkedIn content that converts"
    audience = "founders and operators"
    offer = "your service or launch"

    print("=== CHEF Framework ===")
    for k, v in writer.chef_framework().items():
        print(f"{k}: {v}")

    print("\n=== 70-20-10 Content Mix (10 posts) ===")
    print(writer.content_mix(10))

    print("\n=== Sample LinkedIn Post ===")
    print(writer.generate_post(topic, audience, offer))

    print("\n=== Carousel Script ===")
    for slide in writer.generate_carousel_script(topic):
        print(f"- {slide}")

    print("\n=== Design Guidelines ===")
    print(writer.design_guidelines())


if __name__ == "__main__":
    main()


