const Grid = MaterialUI.Grid;
const Typography = MaterialUI.Typography;

function App() {
    return (
        <div className="main">
            <Grid container justify="center" spacing={3}>
                <Grid item xs={10} sm={8}>
                    <h1 className="heading">WA Covid Vaccines</h1>
                    <Appointments />
                    <Typography className="footer" variant="caption" display="block" gutterBottom>
                        Copyright &#169; {new Date().getFullYear()} Evan Mazor. All rights reserved.
                    </Typography>
                </Grid>
            </Grid>
        </div>
    )
}
