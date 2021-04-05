from examples.writing_tools import run_essay_intro, run_essay_outline, run_poem_creator, run_simplify_sentences
from examples.Website_Copy import run_blog_ideas, run_blog_intro, run_blog_outline, run_listicle, run_meta_descript,  run_microcopy, run_subheader, run_web_landing
from examples.Social_Media import run_brainstorm_topics, run_bullet_points, run_call_to_action, run_caption_generator, run_carousel_post, run_keyword_generator, run_launch_your_prod, run_product_showcase, run_short_text_hook, run_video_intro_hook, run_video_titles, run_YT_descript
from examples.Social_Ads import run_google_headlines, run_ig_captions
from examples.Sales_Copy import run_aida_app, run_sales_copy, run_before_after_bridge, run_feature_adv_bene, run_feature_benefits, run_marketeing_angles, run_pas, run_prob_prom_proof
from examples.product_descriptions import run_product_descript
from examples.personal_tools import run_cover_letter, run_resume_bullet_points, run_social_bio
from examples.other_examples import run_analogies_app, run_blank_example, run_command_to_email_app, run_general_knowledge_q_and_a_app, run_latex_app, run_recipe_app
from examples.Email_Templates import run_catchy_subject_line, run_cold_email_first_lines, run_confirmation_email, run_thank_you_note
from examples.brain_storming_tools import run_growth_ideas, run_next_product, run_start_up_ideas, run_viral_ideas

models = [
    run_essay_intro, run_essay_outline, run_poem_creator, run_simplify_sentences,
    run_blog_ideas, run_blog_intro, run_blog_outline, run_listicle, run_meta_descript,  run_microcopy, run_subheader, run_web_landing,
    run_brainstorm_topics, run_bullet_points, run_call_to_action, run_caption_generator, run_carousel_post, run_keyword_generator, run_launch_your_prod, run_product_showcase, run_short_text_hook, run_video_intro_hook, run_video_titles, run_YT_descript,
    run_google_headlines, run_ig_captions,
    run_aida_app, run_sales_copy, run_before_after_bridge, run_feature_adv_bene, run_feature_benefits, run_marketeing_angles, run_pas, run_prob_prom_proof,
    run_product_descript,
    run_cover_letter, run_resume_bullet_points, run_social_bio,
    run_analogies_app, run_blank_example, run_command_to_email_app, run_general_knowledge_q_and_a_app, run_latex_app, run_recipe_app,
    run_catchy_subject_line, run_cold_email_first_lines, run_confirmation_email, run_thank_you_note,
    run_growth_ideas, run_next_product, run_start_up_ideas, run_viral_ideas
]

# build model loopup table
modelLookup = {}
for model in models:
    modelLookup[model.id] = model