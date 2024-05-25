import requests
 
def fetch_top_models():
    response = requests.get('https://huggingface.co/api/models')
    models = response.json()
    
    # Sort models by the download count and get the top 10
    top_models = sorted(models, key=lambda x: x.get('downloads', 0), reverse=True)[:10]
    return top_models
 
def generate_report(top_models):
    report = "Top 10 Downloaded Models on Hugging Face:\n\n"
    for i, model in enumerate(top_models, 1):
        report += f"{i}. {model['modelId']} - {model.get('downloads', 0)} downloads\n"
    
    with open('report.txt', 'w') as f:
        f.write(report)
 
def main():
    top_models = fetch_top_models()
    generate_report(top_models)
 
if __name__ == "__main__":
    main()