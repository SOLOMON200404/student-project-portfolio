# Day 5 — Time Stone: saved worksheet values

Console snapshot: GS-9 Segment Strike scored 19; GS-10 14 Million Futures scored 16; ID-9 Segment Snipe submitted; ID-10 Fake or Fact II remained Open; L5 Time Loop scored 17; ST-5 Futures Report scored 15.

## L5 / M3-1 Time Loop Results

The nine saved results are exported in `M3-1_Results.csv`.

### RFM instructions recorded in the console

- Recency days: `=DATE(2026,10,1)-F2`
- R score: `=IF(K2<=30,3,IF(K2<=90,2,1))`
- F score: `=IF(G2>=8,3,IF(G2>=3,2,1))`
- M score: `=IF(H2>=600,3,IF(H2>=200,2,1))`
- Segment formula: Champions (R=3,F=3); At risk (R=1,F>=2); New (R=3,F=1); Hibernating (R=1,F=1); Promising (R=2,F=1); otherwise Loyal.
- RFM output is for D4 fictional practice customers; not Duolingo users.

### Churn model caveat

The console lists the Orange workflow steps as checked, but the saved results explicitly say the metrics came from a **scikit-learn practice alternative**, not an Orange run. The numerical comparison and confusion counts are stored in `M3-1_Results.csv`. D5 data are fictional practice subscribers.

### CRM and lifecycle tools

The console records the sample Sheets alternative as completed for counting segments, while **HubSpot's live import/segment was not completed**. MailerLite signup was blocked by rate-limit/human verification; no automation was created. No paid plan was used. These are documented as limitations rather than claimed as live implementations.
