# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


class BrowerHistory:

    def __init__(self, homepage):
        self.history = [homepage]
        self.current = 0
    
    def visit(self, url):
        self.history = self.history[:self.current+1]
        self.history.append(url)
        self.current += 1
    
    def back(self, steps):
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps):
        self.current = min(len(self.current) - 1, self.current + steps)
        return self.history[self.current]

    def get_history(self):
        back_page = self.history[:self.current]
        current_page = self.history[self.current]
        forward_page = self.history[self.current + 1:]
        print("back_pages: "+str(back_page))
        print("current_page: "+str(current_page))
        print("forward_page: "+str(forward_page))


browser_history = BrowerHistory("google.com")
browser_history.visit("cricbuzz.com")
browser_history.visit("gaana.com")
browser_history.visit("spotify.com")

print("going back to 1 step: "+browser_history.back(1))
print("going back to 2 step: "+browser_history.back(1))

browser_history.get_history()