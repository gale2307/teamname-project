from transformers import BertForQuestionAnswering
from transformers import BertTokenizer
from f1score import get_metric_score
import bert_class

model = BertForQuestionAnswering.from_pretrained('deepset/bert-large-uncased-whole-word-masking-squad2')
tokenizer = BertTokenizer.from_pretrained('deepset/bert-large-uncased-whole-word-masking-squad2')

total_score = 0.0

with open("bert_eval.txt", "r") as file:
    for line in file:

        question, context, answers = line.split('|', 2)
        gold_answers = answers.split('|')

        if context[:13] != "MinecraftWiki/": context = "MinecraftWiki/" + context

        print("question: " + question)

        #ask the question to the model
        #receive predicted answer from model
        model_answer, model_score = bert_class.answerfromwebpage(question, context, model, tokenizer)

        print(gold_answers)
        score = get_metric_score(model_answer, gold_answers)
        #print question and score
        print("answer: " + model_answer)
        print("score: " + str(score))
        total_score+=score[1]

print("Total score: " + str(total_score))