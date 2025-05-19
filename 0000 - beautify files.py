# This script fetches LeetCode problem details and adds them to the top of each Python file in the current directory.

import os
import requests


def fetch_all_problems():
    url = "https://leetcode.com/api/problems/all/"
    response = requests.get(url)
    return response.json()['stat_status_pairs']

def find_problem_title_slug_by_number(number):
    problems = fetch_all_problems()
    for p in problems:
        if int(p['stat']['frontend_question_id']) == number:
            return p['stat']['question__title_slug']
    return None

def get_problem_details(title_slug):
    url = "https://leetcode.com/graphql"
    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        difficulty
        content
        likes
        dislikes
      }
    }
    """
    variables = {"titleSlug": title_slug}
    response = requests.post(url, json={'query': query, 'variables': variables})
    return response.json()

def get_problem_url_by_number(problem_number):
    slug = find_problem_title_slug_by_number(problem_number)
    if slug:
        return f"https://leetcode.com/problems/{slug}/"
    return None

def details_of_problem(number):
    slug = find_problem_title_slug_by_number(number)
    if slug:
        details = get_problem_details(slug)
        url = get_problem_url_by_number(number)
        title = details['data']['question']['title']
        difficulty = details['data']['question']['difficulty']
        return {
            "title": title,
            "difficulty": difficulty,
            "url": url
        }
    return None

def main():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files.remove(os.path.basename(__file__))
    for file in files:
        if file.endswith('.py'):
            with open(file, 'r+') as f:
                content = f.read()
                lines = content.split('\n')
                if lines[0].startswith('# URL: '): continue
                details = details_of_problem(int(file.split('.')[0]))
                if not details: continue
                else:
                    content = f"# URL: {details['url']}\
                        \n# TITLE: {details['title']}\
                            \n# DIFFICULTY: {details['difficulty'].title()}\
                                \n# ------------------------------------------------------\n" + content
                    f.seek(0)
                    f.write(content)
        elif file.endswith('.cs'):
            with open(file, 'r+') as f:
                content = f.read()
                lines = content.split('\n')
                if lines[0].startswith('// URL: '): continue
                details = details_of_problem(int(file.split('.')[0]))
                if not details: continue
                else:
                    content = f"// URL: {details['url']}\
                        \n// TITLE: {details['title']}\
                            \n// DIFFICULTY: {details['difficulty'].title()}\
                                \n// ------------------------------------------------------\n" + content
                    f.seek(0)
                    f.write(content)

if __name__ == "__main__":
    main()
