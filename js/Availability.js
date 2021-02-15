function Availability({ scrape }) {
    if (!scrape.available) {
        return <div className="availability no-availability">
            Not available</div>
    } else if (typeof scrape.num_appointments == 'undefined') {
        if (scrape.walk_in) {
            return <div className="availability">
                Walk-in availabile</div>
        } else {
            return <div className="availability">
                Appointments availabile</div>
        }
    } else {
        return <div className="availability">
            {scrape.num_appointments} Appointments available</div>
    }
}
