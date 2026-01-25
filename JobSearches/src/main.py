from src.cv_reader import read_cv_text
from src.profile_builder import extract_profile_from_cv
from src.job_finder import find_jobs_matching_profile
from src.job_parser import format_jobs_for_display

def run_job_search(cv_path):
    print("Reading CV...")
    cv_text = read_cv_text(cv_path)

    print("Building profile from CV...")
    profile = extract_profile_from_cv(cv_text)

    print("Searching for matching jobs...")
    jobs = find_jobs_matching_profile(profile)

    print("Formatting results...\n")
    result_text = format_jobs_for_display(jobs)

    print(result_text)

if __name__ == "__main__":
    run_job_search("data/my_cv.txt")
