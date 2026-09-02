from pathlib import Path
import json, time
import pandas as pd

from tasks.task_a import run_task_a
from tasks.task_b import run_task_b
from tasks.task_c import run_task_c
from tasks.task_d import run_task_d
from tasks.task_e import run_task_e
from tasks.task_f import run_task_f
from tasks.task_g import run_task_g

ROOT=Path(__file__).resolve().parent
RAW=ROOT/"data/raw/benchmark_crop_climate.csv"
RESULTS=ROOT/"results"

def main():
    start=time.perf_counter()
    a=run_task_a(RAW, RESULTS)
    b=run_task_b(a["X_train"],a["y_train"],a["X_val"],a["y_val"],a["X_test"],a["y_test"],RESULTS)
    c=run_task_c(a["X_train"],a["y_train"],a["X_val"],a["y_val"],a["X_test"],a["y_test"],RESULTS)
    d=run_task_d(a["data"],a["train"],RESULTS)
    e,kdtree=run_task_e(RESULTS)
    run_task_f(a["data"],b["validation"][b["validation"]["metric"]=="euclidean"],c["validation"],e,[{"Model":"kNN",**b["metrics"]},{"Model":"LWR",**c["metrics"]}],RESULTS)
    g=run_task_g(a["test"],a["y_test"],b["pred"],c["pred"],RESULTS)
    summary={"raw_rows":len(pd.read_csv(RAW)),"clean_rows":len(a["data"]),"train_rows":len(a["train"]),"validation_rows":len(a["validation"]),"test_rows":len(a["test"]),"knn_best_metric":str(b["best"]["metric"]),"knn_best_k":int(b["best"]["k"]),"knn_test_metrics":b["metrics"],"lwr_best_tau":c["best_tau"],"lwr_test_metrics":c["metrics"],"total_seconds":time.perf_counter()-start}
    (RESULTS/"logs").mkdir(parents=True,exist_ok=True)
    (RESULTS/"logs/final_interlinked_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print(json.dumps(summary,indent=2))
    print("\nA -> B -> C -> D -> E -> F -> G completed successfully.")

if __name__=="__main__": main()
