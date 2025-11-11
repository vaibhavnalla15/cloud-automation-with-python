
| Mistake                                   | Explanation                                              | Fix                                                    |
| ----------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------ |
| Wrong indentation inside loop             | You had nested parsing incorrectly under the wrong block | Align `cpu, mem` parsing with `for log in alert_logs:` |
| Mixed variable names (`line`, `new_date`) | You reused `line` inside the wrong scope                 | Use `log` consistently                                 |
| Hardcoded `new_date`                      | You used a static date instead of extracting from file   | Split the line to extract actual date                  |
| Missing `.strip()`                        | Some lines may have newline characters                   | Always `.strip()` before parsing                       |
| No validation for `ALERT:` format         | Would fail if line missing `ALERT:`                      | Add simple check before splitting                      |

