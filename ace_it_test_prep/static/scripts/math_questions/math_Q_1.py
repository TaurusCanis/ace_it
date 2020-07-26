import random
names = ["Tom", "Lindsay"]
items = ["marbles", "sticks"]
vars = ["x", "y", "z"]
situation = ["more", "fewer"]
name_1 = names[random.randint(0,len(names) - 1)]
name_2 = names[random.randint(0,len(names) - 1)]
while name_2 == name_1:
    name_2 = names[random.randint(0,len(names) - 1)]
item = items[random.randint(0,len(items) - 1)]
var_name = vars[random.randint(0,len(vars) - 1)]
more_or_fewer = situation[random.randint(0,len(situation) - 1)]
num_of_name_2_var = random.randint(3,8)
if more_or_fewer == "more":
    answer = f"{num_of_name_2_var} + {var_name}"
    options = [
        {
            "option": answer,
            "correct": True
        },
        {
            "option": "\\(\\frac{k}{7}\\)",
            "correct": False
        },
        {
            "option": "\\(\\frac{7}{k}\\)",
            "correct": False
        },
        {
            "option": "<em>k&nbsp;</em>- 7",
            "correct": False
        },
        {
            "option": "7 -&nbsp;<em>k</em>",
            "correct": False
        }
    ]
else:
    answer = f"{num_of_name_2_var} - {var_name}"
    options = [
        {
            "option": answer,
            "correct": True
        },
        {
            "option": "\\(\\frac{k}{7}\\)",
            "correct": False
        },
        {
            "option": "\\(\\frac{7}{k}\\)",
            "correct": False
        },
        {
            "option": "<em>k&nbsp;</em>- 7",
            "correct": False
        },
        {
            "option": "7 +&nbsp;<em>k</em>",
            "correct": False
        }
    ]
# Need to include this in above dicts
# distractor_rationale = [
# "You may have taken the unknown score to be given as a fraction of Anna's score, but the term \"fewer\" indicates that the difference is based on subtraction.",
# "You may have taken the unknown score to be given as a ratio of Anna's score to the difference, but the term \"fewer\" indicates that the difference is based on subtraction.",
# "You identified a score that is 7 points fewer than <em>k&nbsp;</em>points, but the expression must represent&nbsp;<em>k&nbsp;</em>points fewer than 7.",
# "The number of points Franz scored is the difference between 7 and&nbsp;<em>k</em>, since Franz scored&nbsp;<em>k&nbsp;</em>fewer points&nbsp;fewer.",
# "You identified a score representing&nbsp;<em>k&nbsp;</em>points more that Anna's score, rather than&nbsp;<em>k&nbsp;</em>points fewer."
# ]

random.shuffle(options)

question_text = f"<p>{name_1}&nbsp;has <strong><em>{var_name}</em></strong><em>&nbsp;</em>{more_or_fewer} {item} &nbsp;than {name_2}. {name_2} has {num_of_name_2_var} {item}. How many {item} does {name_1}&nbsp;have, in terms of <strong><em>{var_name}</em></strong>?&nbsp;</p>\n"
print(question_text)

letter_index = 65
for option in options:
    print(chr(letter_index) + ": " + option["option"])
    letter_index += 1

user_response = input("Choose and answer option: ")
if options[ord(user_response.upper()[0]) - 65]["correct"]:
    print("CORRECT!")
else:
    print("INCORRECT!")

testSectionItemIds = [
"f6ce66f7-bdfa-48db-ba7e-75fff87c909b",
"cad4ddca-2497-4935-88b9-910beacd4454",
"5a04df0a-d123-49c2-bc2d-6228c29d85e1",
"07d8d5f7-85a8-40fd-ae4e-6b1b12a480de",
"c4b8c7bf-b807-4d87-b8d5-d87cdcc675d3",
"1b8aa3b3-f077-49df-9698-984d4e881e13",
"60d811b5-6a15-4c2a-8f14-3410a61fb6bc",
"aac4cc29-5ae8-4114-a188-d8b7366a921b",
"2d93fd69-656c-4332-9cf5-a12d63496515",
"26f27347-5b68-4a2d-b546-6da06fcf7017",
"c91aa7a8-cde8-4c07-b2e1-7d917cf60663",
"402dd3b6-a97a-491b-b3c1-0745f9b53472",
"e898e6c2-3f33-49e0-8d26-b65765f5fd0e",
"ace09695-e7bd-43fb-b7da-2ed0506dec90",
"4bb201a9-c7a3-4558-8a24-105a33e9c695",
"5c5c9f24-d864-459e-b264-4cc860b02581",
"33314609-b6a0-4665-9b62-9179f6b82169",
"c182a445-42c4-4eb1-adfc-cbc1bf9f1333",
"0ef74e74-9151-4344-a579-153802f20eb9",
"f2703b05-b4cc-49c2-937f-77eee7f94af6",
"d9c4902d-9ad4-4141-bca1-af13fe3fdaea",
"9425df42-45a9-4f5a-ace3-525f4b67daa3",
"42c5c09f-2bc2-44eb-b60a-9690b8396742",
"937b0379-594d-4803-b752-d524a89ed8f3",
"39ae8d09-c622-4856-9964-9723a20a914c",
"28d1294c-5c70-4f49-b32d-adca050ed63f",
"e4531b92-b6a1-43c5-8658-7b3424715b5c",
"a8a84a52-ef98-4eac-bf9b-92bb23854206",
"da1d699f-fcf4-4f02-9509-ad8e510ccc91",
"aaf174db-ba77-49c8-b9d4-dbeafb62d019",
"a0fb3076-b1cf-4c3e-9d1d-367c0ba4646a",
"55d13874-b063-4896-935e-65a144420f0c",
"875d5205-282f-473b-a030-7a2b9e00c73c",
"89a1c7f7-b50c-466c-9c4c-a68c94a24b88",
"75bdb2a6-fce1-4ce0-af44-75a33576e6ad",
"c6a9b974-1bad-41af-8b8f-467a5404da99",
"551105b0-ba13-4815-86b1-ea6a6991f40a",
"fd1f7fa6-d479-46c4-8c51-d7bc8f66c999",
"ca2d46e9-836b-45bd-8db4-01cc7ee3133f",
"f22297a1-5267-41f1-96a6-73217a3148ce",
"1a2c4b46-33f4-4b46-b96b-528b51a5e96d",
"95184c77-4fa2-4f86-96f0-7b202e0cb077",
"eb925ddc-5812-4d25-b71c-a05e7ac2c91b",
"0cdd02f4-b7f7-4ec4-a1de-8081d07e3bd4",
"c982eaf7-a682-4633-a389-8be677c45b60",
"98c4ecbc-b2aa-49b9-999d-9438097cc174",
"757f695a-990e-4051-83e4-6aa97e917613",
"97f63132-63e4-42f0-b5e2-8bf7f96f6f23",
"c71637f5-d092-4e98-bc57-f473a3b8eb60",
"51a2f66b-0b13-4efa-ac3e-0a89a48b24e3",
"846c2a7a-d571-4bf0-834b-b1f48d881cc3",
"03ad4d2e-1c9d-4e04-a973-28db2275e2fd",
"51fedcc5-9f6c-412b-b605-51a7d00f9d80",
"dd92e533-8e6d-4be5-a223-755f3eb71e99",
"f2e977d5-9358-41d4-b853-3d138cda37cf",
"c58da06f-6a3c-4d44-979a-3748542912c0",
"5b88f374-5806-435d-a5c2-b77878505681",
"7346be17-e947-417a-b25a-c8566bfd00d0",
"55a58393-a2bf-4d50-8a82-7b26b78c5432",
"0491657c-aec9-4538-aa29-06c800134298",
"7faea7d1-568a-46c3-b7a3-dcd2abd8aff5",
"7728ca98-c7c7-4b13-b396-4d23c6f88566",
"795a4fa8-c4a3-46e0-9562-2f4bbea93807",
"989dbcef-9ccb-4ff6-9706-9367e07317e7",
"82fa88e6-526b-48fa-b22d-a4d2aecca645",
"aae5bc10-9d41-44b7-8a22-2787cfaef9ab",
"1556d03e-e2d3-4e98-9959-439cc4c57618",
"130819b3-e057-4839-a956-591106e4a8fb",
"1783dc0d-c490-4c1a-ac42-e000a4e7d675",
"4cc08d43-fe48-44c5-ad1e-9946538619c7",
"4d457ab8-1a84-45ba-819c-6915af8afcf9",
"47566d44-a8fa-4037-b666-bf90e82905dd",
"d3ea0860-b328-4885-b1ad-8bcb3b26b7f9",
"ef71355c-cd6e-4171-9c7b-2094ae12d2ba",
"ccfec784-cd7a-4901-8750-fa9d2371090f",
"8a19418e-7aac-4cf7-9449-9a20f457421e",
"59594b1a-9209-47ad-a9fa-797fa0099d15",
"1f9e1a39-1de5-42db-82e9-296cc4364b38",
"cddc4f99-7779-4a74-8a20-fa4e1f8ac630",
"da0ccacd-2072-4199-8574-5221e135ae4f",
"757d03ab-d92d-4221-8d76-dea161c09e87",
"e507ad20-f71d-461f-aecd-81e1cb4978b8",
"32a0ad59-1ff4-4fb9-a2de-3300a942e0cb",
"c4f3d1db-5deb-4708-bf4c-fa3b4ed6cb5e",
"8975ede0-b049-40a7-b472-ae5e8ea895b1",
"e3c1fb33-c0d3-4dd3-b2b3-aee999cb4f39",
"7315241e-940e-44e2-b39e-c6fd4327a7d3",
"ff21a305-8661-4016-99c9-a54187cc8b89",
"26919c2d-7d9a-4e61-9e66-eff702ff6a8d",
"711e8c18-7662-4b8f-b6ac-8c8b5244c735",
"ceafe281-69b3-44fc-8ace-c155864e8f88",
"0d43cc88-15db-4e6f-8ef9-6c1ba360d00a",
"337b0cc4-33c0-4908-8333-97a2d221a727",
"7f31949f-559d-46a7-90b9-27fb98e460a4",
"c127c8aa-44bf-45fa-a5e2-8cf29b45c5ce",
"839e2e0d-83f7-4da9-93a5-7b56e8862237",
"d5183474-9d0e-4306-bcc2-7df97759fd6e",
"476691ee-cea4-4372-a93c-119544aeb864",
"0c0d75c9-0681-4c5f-99a9-080c79f19e42",
"00e010db-2bc0-4f64-ab69-a12326dcad51",
"1a09264a-c9a8-4488-abdd-b324edf3296e",
"119cb218-9c9f-4c23-b7b0-30feddf6006c",
"0c486b57-2f1b-4745-8d63-4018d75921c3",
"3d55cd5e-fff6-4e2a-809e-f5ccdf1ef677",
"af3b9a2c-677e-44c7-ba97-a2858a5bde6e",
"458a6382-e0f6-4931-b8a0-f411f8018e40",
"13933bb7-d631-408c-896c-1a7208aa3dc3",
"688d0440-8048-4500-8ea9-db2cc856383a",
"5f15e164-e961-48e1-ac64-ee9ed195dfd7",
"7ddb8e29-1c31-44aa-80b5-f937e48efb06",
"e849bee6-a2a4-4129-8dbc-98c78bc7f3b8",
"1a167c4e-64bd-45f5-980c-a0978e50c695",
"e58ad2a5-94e0-4eb2-8908-6204a128b6c9",
"b9124400-844e-4960-a87f-ba0f05ab07a7",
"033a76b6-1bac-4c59-9c04-f6adfa39c20d",
"d62587b0-b73b-4d5f-ab85-627bc686c679",
"aa01e5f0-da67-4520-b5c4-edd4fa49dbce",
"9cebefa5-14f3-4eaa-9134-bdcf15802767"
]

print(len(testSectionItemIds))

testSectionItemNKs = [
"SSATP_10708",
"SSATP_07704-UL-P1-S1-5",
"SSATP_07814-UL-P1-S4-21",
"SSATP_07739-UL-P1-S1-13",
"SSATP_07701_UL-P1-S1-3",
"SSATP_07759-UL-P1-S1-24",
"SSATP_09747",
"SSATP_07806-UL-P1-S4-15",
"SSATP_09748",
"SSATP_07738-UL-P1-S1-12",
"SSATP_07805-UL-P1-S4-14",
"SSATP_09749",
"SSATP_07758-UL-P1-S1-23",
"SSATP_07818-UL-P1-S4-23",
"SSATP_07791-UL-P1-S4-1",
"SSATP_07815-UL-P1-S4-22",
"SSATP_09750",
"SSATP_09751",
"SSATP_09752",
"SSATP_09753",
"SSATP_07754-UL-P1-S1-20",
"SSATP_07813-UL-P1-S4-20",
"SSATP_09754",
"SSATP_09755",
"SSATP_09756",
"SSATP_07761-UL-P1-S2-Set1",
"SSATP_07763-UL-P1-S2-Set2",
"SSATP_07765-UL-P1-S2-Set3",
"SSATP_07766-UL-P1-S2-Set4",
"SSATP_07768-UL-P1-S2-Set5",
"SSATP_09825",
"SSATP_07770-UL-P1-S2-SetSeven",
"SSATP_07771-UL-P1-S2-Set8",
"SSATP_09772",
"STAGE_00250-UL-P1-S3-14",
"SSATP_09773",
"SSATP_09774",
"SSATP_09775",
"SSATP_09776",
"SSATP_09777",
"STAGE_00252-UL-P1-S3-16",
"SSATP_09778",
"STAGE_00242-UL-P1-S3-10",
"STAGE_00238-UL-P1-S3-7",
"STAGE_00261-UL-P1-S3-23",
"SSATP_09779",
"STAGE_00251-UL-P1-S3-15",
"STAGE_00259-UL-P1-S3-22",
"SSATP_09780",
"STAGE_00265-UL-P1-S3-26",
"SSATP_09781",
"SSATP_09782",
"SSATP_09783",
"STAGE_00254-UL-P1-S3-18",
"SSATP_09785",
"SSATP_09786",
"SSATP_09787",
"SSATP_09788",
"SSATP_09789",
"SSATP_09790",
"SSATP_09791",
"SSATP_09792",
"SSATP_09793",
"SSATP_09794",
"SSATP_09795",
"SSATP_09796",
"SSATP_09797",
"SSATP_09798",
"SSATP_09799",
"SSATP_09800",
"SSATP_09801",
"SSATP_09802",
"STAGE_00279-UL-P1-S3-36",
"SSATP_09803",
"SSATP_09804",
"SSATP_09805",
"SSATP_09806",
"SSATP_09807",
"SSATP_09808",
"SSATP_09809",
"SSATP_09810",
"SSATP_09811",
"SSATP_09812",
"SSATP_09813",
"SSATP_09814",
"SSATP_09815",
"SSATP_09816",
"SSATP_09817",
"SSATP_09818",
"SSATP_09820",
"SSATP_09821",
"SSATP_09822",
"SSATP_09823",
"SSATP_09757",
"SSATP_07792-UL-P1-S4-2",
"SSATP_07703",
"SSATP_09758",
"SSATP_09892",
"SSATP_09760",
"SSATP_07709-UL-P1-S1-8",
"SSATP_09761",
"SSATP_07742_UL-P1-S1-14",
"SSATP_07757-UL-P1-S1-22",
"SSATP_09762",
"SSATP_09763",
"SSATP_07799-UL-P1-S4-8",
"SSATP_09764",
"SSATP_09765",
"SSATP_07760-UL-P1-S1-25",
"SSATP_09766",
"SSATP_09767",
"SSATP_09768",
"SSATP_07819-UL-P1-S4-24",
"SSATP_07811-UL-P1-S4-18",
"SSATP_09769",
"SSATP_09770",
"SSATP_09771",
"SSATP_07746-UL-P1-S1-17"
]

print(len(testSectionItemNKs))
