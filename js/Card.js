const Button = MaterialUI.Button;
const CardContent = MaterialUI.CardContent;
const Grid = MaterialUI.Grid;
const Typography = MaterialUI.Typography;

const Card = ({ scrape }) => {
    if (typeof scrape === 'undefined') {
        return <h3>Loading</h3>;
    }

    const classes = MaterialUI.makeStyles({
        card: {
            marginBottom: "1rem",
            border: "1px solid gray"
        },
        reserveButton: {
            width: "100%",
        },
    })();

    const { available, name, num_appointments, time, url } = scrape;
    const numAppointments = typeof num_appointments == 'undefined' ? 0 : num_appointments;

    return (
        <MaterialUI.Card elevation={0} className={classes.card}>
            <CardContent>
                <Grid container spacing={3} display="flex">
                    <Grid item xs={12} sm={6} className={classes.column}>
                        <Typography variant="h5" component="h2">
                            {name}
                        </Typography>
                        <Typography className={classes.pos} color="textSecondary">
                            Address
                        </Typography>
                    </Grid>
                    <Grid item xs={12} sm={3}>
                        <Typography
                            variant="overline"
                            display="inline"
                            className="show-small-inline"
                        >
                            Updated:
                        </Typography>
                        <Typography variant="overline" display="inline">
                            <u>Updated:</u><br></br>
                        </Typography>
                        <Typography variant="overline" display="inline">
                            {Math.round(Date.now()/1000 - time)} seconds ago
                        </Typography>
                    </Grid>
                    <Grid item xs={12} sm={3}>
                        <Button
                            size="medium"
                            variant="contained"
                            color="primary"
                            className={classes.reserveButton}
                            disabled={!available}
                            href={url}
                        >
                            {available ? "Reserve" : "No Appointments"}
                        </Button>
                        {(numAppointments !== 0) ?
                        <Typography>
                            {numAppointments} Appointments
                        </Typography> : null}
                    </Grid>
                </Grid>
            </CardContent>
        </MaterialUI.Card>
    );
}
