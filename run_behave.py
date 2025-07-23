import sys
import argparse
from behave.__main__ import main as behave_main


def build_behave_args(tags, browser, headless, report):
    args = ['features']
    if tags:
        args += ['-t', tags]
    if report:
        args += ['--format', 'pretty', '--outfile', report]
    if browser:
        args += ['-D', f'browser={browser}']
    if headless:
        args += ['-D', 'headless=true']
    return args
def main():
    parser = argparse.ArgumentParser(description='Run Behave BDD tests with options.')
    parser.add_argument('--tags', type=str, help='Tag to filter scenarios')
    parser.add_argument('--browser', type=str, default='chrome', help='Browser to use')
    parser.add_argument('--headless', action='store_true', help='Run in headless mode')
    parser.add_argument('--report', type=str, default='report.html', help='Report file name')
    args = parser.parse_args()

    behave_args = build_behave_args(args.tags, args.browser, args.headless, args.report)
    sys.exit(behave_main(behave_args))

if __name__ == "__main__":
    main()