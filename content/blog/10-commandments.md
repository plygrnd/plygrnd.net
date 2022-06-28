+++
title = "The 9 Commandments of Coordinated Vulnerability Disclosure"
date = "2022-02-03T21:47:17-05:00"

description = "The 9 Commandments of Coordinated Vulnerability Disclosure."

tags = ["cvd"]
+++

This was originally a [Twitter thread](https://twitter.com/notdurson/status/1489350457730469888). In case Twitter goes the way of the dodo, I'll preserve the content here (with some edits now that I'm no longer limited to 280 characters per point).

The nine points below capture, at a high level, most of what I know about responsible disclosure/CVD/the ins and outs of reporting security issues in other people’s software.


1. Operate with good intentions in mind. You're hacking on other people’s stuff (and presumably doing so for the common good). Treat other people's infrastructure like you treat your phone/wallet/car/favorite plushie - respect it and try not to break it. If your targets publish rules of engagement, follow them to the letter.
1. Be verbose - more info is better. Don't assume that anyone will know what you're reporting from context. Include as many details and as much background as possible in your report.
1.  Produce - *and provide* - a proof of concept which bears out your assertions. Decent  incident responders won't balk at reading a 10 page description of your findings. If they can't reproduce them, though, they can't help you.
1. Be prepared for disappointment. Bug hunting is hard, painful, irritating work which may be thrown away as "known issue" or "won't fix" or "accepted risk". It happens - and it's not personal. 
1. People are fallible. Everyone's wrong sometimes. If you disagree with a decision not to accept a report or fix an issue, and you have compelling evidence to indicate that your findings are valid, fight for yourself. Escalate if you need to. But - be nice about it.
1. Be prepared to go unrewarded - it'll make the first bounty feel that much better. Rewards are nice, but not mandatory. Bounties are at the vendor's discretion.
1. Act with integrity. Badgering or threatening vendors to extract a reward isn't responsible disclosure. It's extortion. Such behavior might result in your report being downplayed. It can also get you removed from bug bounty programs or banned from using the service you researched.
1. If you're confident in your findings, include a disclosure date in your report and be upfront about your disclosure plan (blog/tweet/other). This keeps everyone on the same page and helps the responding party determine the scope/pace of their work.
1. Above all, have some fun. Get to know the teams you report stuff to - we love making new friends :)
