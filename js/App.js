const useStyles = MaterialUI.makeStyles({
    container: {
        maxWidth: "800px",
        padding: "1rem",
        margin: "0 auto",
    },
    nav: {
        textAlign: "center",
        padding: 0,
    },
    li: {
        display: "inline-block",
        margin: "1rem",
    },
    a: {
        textDecoration: "none",
    },
    footerText: {
        fontSize: ".75rem",
        textAlign: "center",
        margin: "3rem",
    },
});

function App() {
    const classes = useStyles();

    return (
        <div className={classes.container}>
            <nav>
                <ul className={classes.nav}>
                    <li className={classes.li}>
                        <Appointments className={classes.a} />
                    </li>
                </ul>
            </nav>
        </div>
    )
}
