browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)

print(browsing_session.pop())
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
  print("disable")