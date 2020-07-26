import random

question = f"<p>If \\(\\frac{1}{5}+x&gt;1\\)&nbsp;, which of the following could be the value of \\(x\\) ?</p>\n"

options = [
    {
    "label":"\\(\\frac{1}{5}\\)",
    "value":"0"
    },
    {
    "label":"\\(\\frac{2}{5}\\)",
    "value":"1"
    },
    {
    "label":"\\(\\frac{1}{2}\\)",
    "value":"2"
    },
    {
    "label":"\\(\\frac{2}{3}\\)",
    "value":"3"
    },
    {
    "label":"\\(\\frac{9}{10}\\)",
    "value":"4"
    }
]

# "distractor_rationale_response_level":[
# "You may have attempted to solve \\(\\left(\\frac{1}{5}\\right)\\div x=1\\)&nbsp; instead of \\(\\frac{1}{5}+x&gt;1\\)&nbsp;",
# "You may have attempted to solve \\(\\frac{1}{5} &lt; x &lt; 1\\)&nbsp; instead of \\(\\frac{1}{5}+x&gt;1\\)&nbsp;",
# "You may have attempted to solve \\(\\frac{1}{5}+x &lt; 1\\)&nbsp; instead of \\(\\frac{1}{5}+x&gt;1\\)&nbsp;.",
# "You may have taken&nbsp;\\(\\frac{2}{3}\\) to be greater than \\(\\frac{4}{5}\\), but&nbsp;\\(\\frac{2}{3}=\\frac{10}{15}\\) and \\(\\frac{4}{5}=\\frac{12}{15}\\).",
# "If \\(\\frac{1}{5}+x&gt;1\\), then \\(x&gt;\\frac{4}{5}\\). This is the result of subtracting&nbsp;\\(\\frac{1}{5}\\) from both sides of the inequality. Since&nbsp;\\(\\frac{4}{5}=\\frac{8}{10}\\), \\(\\frac{9}{10}&gt;\\frac{4}{5}\\). So,&nbsp; \\(\\frac{9}{10}\\)could be the value of&nbsp;<em>x</em>."
# ]
