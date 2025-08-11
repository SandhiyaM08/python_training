raw_guests=['alice','','Bob','ALICE','bob','Eve','eve','',' ANAND']
result= {
    guest.strip().capitalize(): len(guest.strip())
    for guest in raw_guests
    if guest.strip()  
}
print(result)
