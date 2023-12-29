from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            escaped_email = self.escapeEmail(email)
            email_set.add(escaped_email)

        print(email_set)
        return len(email_set)

    def escapeEmail(self, email: str) -> str:
        parts = email.split("@")
        local = parts[0]
        domain = parts[1]

        # remove dots
        no_dots = "".join(local.split("."))

        res = no_dots + "@" + domain

        # remove right part of +
        idx = no_dots.find("+")

        if idx >= 0:
            res = no_dots[:idx] + "@" + domain

        return res

s = Solution()
s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])