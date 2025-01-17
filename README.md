# ReDoS Checks

This is a simple repository to check if a language / regex engine is vulnerable to ReDoS. If you've written a regular expression with catastrophic backtracking, you may be vulnerable to DoS via a text input that exploits that regular expression.

[`redos.json`][redos-file] contains a collection of vulnerable regular expressions, and text inputs that exploits the vulnerabilities.

[The "ReDoS Checks" action ![ReDoS Checks](https://github.com/spenserblack/redos-checks/actions/workflows/main.yml/badge.svg)][action] executes simple implementations to execute the vulnerable regular expression on the dangerous input, timing out if it takes too long.

[action]: https://github.com/spenserblack/redos-checks/actions/workflows/main.yml
[redos-file]: ./redos.json
